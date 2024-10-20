import re

# Load the requests file
def load_requests(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to capture the requester's name and their songs
    pattern = re.compile(r'\[(?P<person>.+?):\s*(?P<songs>[^\]]+)\]')
    
    # Dictionary to store the requests
    requests = {}
    
    for match in pattern.finditer(content):
        person = match.group('person')
        songs = match.group('songs').split(',')
        
        # Process each song and its artist
        song_artist_pairs = []
        for song in songs:
            if ';' in song:
                song_name, artist = map(str.strip, song.split(';'))
                song_artist_pairs.append((song_name, artist))
        
        requests[person] = song_artist_pairs
    
    return requests

# Example usage
file_path = r'C:\Users\lucas\iCloudDrive\Desktop\Folders\Coding\CumpleLatino\Txt\requests.txt'
requests = load_requests(file_path)

# Print the parsed data
for person, songs in requests.items():
    print(f"Request Person: {person}")
    for song, artist in songs:
        print(f"  - Song: {song}, Artist: {artist}")
