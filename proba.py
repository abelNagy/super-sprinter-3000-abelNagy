import csv


def get_stories():
    with open('/home/abel/codecool/super-sprinter-3000-abelNagy/data.csv', 'r') as csv_file:
        csv_stories = [story for story in csv.reader(csv_file)]
    return csv_stories


def create_id():
    stories = get_stories()
    if stories:
        most_recent_id = stories[0][0]
        for story in stories:
            if int(story[0]) > int(most_recent_id):
                most_recent_id = story[0]
        return int(most_recent_id) + 1
    else:
        return 1


def new_id():
    stories = get_stories()
    last_story = None
    for last_story in stories:
        pass
    if last_story:
        return int(last_story[0]) + 1
    else:
        return 1


def update_stories(story):
    with open('/home/abel/codecool/super-sprinter-3000-abelNagy/data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for story in stories:
            writer.writerow(story)


def overwrite(stories):
    with open('/home/abel/codecool/super-sprinter-3000-abelNagy/data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for story in stories:
            csv_writer.writerow(story)


def route_delete_story(story_id):
    stories = get_stories()
    for story in stories:
        if story[0] == story_id:
            stories.remove(story)
            
            update_stories(story)
    print('/')


stories = get_stories()
print(stories)
route_delete_story("1")
