from flask import Flask, render_template, redirect, request
import csv


app = Flask(__name__)


def get_stories():
    with open('data.csv', 'r', newline='') as csv_file:
        csv_stories = [story for story in csv.reader(csv_file)]
    return csv_stories


def create_story(story_to_add):
    with open('data.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(story_to_add)


def update_stories(stories):
    with open('data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for story in stories:
            writer.writerow(story)


# BUG?: when deleting story and adding a new story, new ID is not the "old" ID
def create_story_id():
    stories = get_stories()
    if stories:
        most_recent_id = stories[0][0]
        for story in stories:
            if int(story[0]) > int(most_recent_id):
                '''
                if int(story[0]) > int(most_recent_id) + 1 and int(most_recent_id) not in stories:
                    return int(most_recent_id) + 1
                '''
                most_recent_id = story[0]
        return int(most_recent_id) + 1
    else:
        return 1


@app.route("/")
def route_index():
    stories = get_stories()
    return render_template('list.html', stories=stories)


@app.route("/list")
def route_list():
    return route_index()


@app.route("/story")
def route_story():
    return render_template('form.html', story=None)


@app.route("/save-story", methods=["POST"])
def route_save_story():
    print("POST request received!")
    story_id = create_story_id()
    new_story = [story_id,
                 request.form['title'],
                 request.form['story'],
                 request.form['criteria'],
                 request.form['business_value'],
                 request.form['estimation'],
                 request.form['status']
                 ]
    create_story(new_story)
    return redirect('/')


@app.route("/story/<story_id>")
def route_story_id(story_id):
    stories = get_stories()
    for story in stories:
        if story[0] == story_id:
            return render_template('form.html', story_id=story_id, story=story)
    else:
        return 'Error: ID not found'


# BUG: when only 1 story left, func doesn't delete it
@app.route("/story/<story_id>/delete", methods=["POST"])
def route_delete_story(story_id):
    print('POST request received')
    stories = get_stories()
    for story in stories:
        if story[0] == story_id:
            stories.remove(story)
    if stories:
        update_stories(stories)
    return redirect('/')


@app.route("/story/<story_id>/update", methods=["POST"])
def route_update_story(story_id):
    print("POST request received!")
    stories = get_stories()
    for story in stories:
        if story[0] == story_id:
            story[1] = request.form["title"]
            story[2] = request.form["story"]
            story[3] = request.form["criteria"]
            story[4] = request.form["business_value"]
            story[5] = request.form["estimation"]
            story[6] = request.form["status"]
    update_stories(stories)
    return redirect("/")


if __name__ == "__main__":
    app.secret_key = 'halmaz'
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
