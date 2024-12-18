# Import for JSON handling
import json
# Import for cli arg handling
import sys
# Import for web requests
import urllib.request
# Import for web request errors
import urllib.error

def get_github_data(username):

    # Set url to username in github api
    url = f"https://api.github.com/users/{username}/events"

    # Create request object with url as url
    request = urllib.request.Request(url)
    # Add the header to accept information
    request.add_header('accept', 'application/vnd.github+json')

    try:
        # Attempt to get the data from the request url
        with urllib.request.urlopen(request) as response:
            if response.status == 200:
                data = response.read().decode()
                events = json.loads(data)
                return events
            else:
                print(f"Error: Received status code {response.status}")
                return None
        # Return none if any exceptions are raised
    except urllib.error.HTTPError as e:
        print(f"Error: {e}")
    except urllib.error.URLError as e:
        print(f"Error: {e}")
    return None


def display_events(events):

    # If exceptions we're raised or no activity found
    if not events:
        print('No activity found')
        return
    for event in events:
        event_type = event.get('type')
        repo_name = event.get('repo', {}).get('name')
        # Check that event and repo name found
        if event_type and repo_name:
            # Custom template for pushes
            if event_type == 'PushEvent':
                commit_count = len(event.get('payload', {}).get('commits', []))
                print(f"- Pushed {commit_count} commits to {repo_name}")
            # Custom template for issues
            elif event_type == 'IssuesEvent':
                action = event.get('payload', {}).get('action')
                print(f"- {action.capitalize()} an issue in {repo_name}")
            # Custom template for stars
            elif event_type == 'WatchEvent':
                print(f"- Starred {repo_name}")
            # Template for others
            else:
                print(f"- {event_type} in {repo_name}")

def main():
    # Check for cli args
    if len(sys.argv) != 2:
        print(f"Usage: github_activity <username>")
        return
    # Get username
    username = sys.argv[1]
    # Get events
    events = get_github_data(username)
    # Display events
    display_events(events)

if __name__ == "__main__":
    main()
