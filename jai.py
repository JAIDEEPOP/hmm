import vlc

def play_video_from_link(video_link):
    # VLC player ka object banayein
    player = vlc.MediaPlayer(video_link)

    # Video play karein
    player.play()

    # Thoda sa wait karein taki player video ko load kar sake
    player.set_pause(1)
    player.play()

    # Sabhi available audio tracks ka list nikalein
    audio_tracks = player.audio_get_track_description()

    # Audio tracks ko print karein
    print("Available audio tracks:")
    for track in audio_tracks:
        print(f"Track {track[0]}: {track[1]}")

    # Konsa audio track chunna chahte hain, wo input se lein
    selected_track = int(input("Enter the track number you want to play: "))

    # Audio track ko set karein
    player.audio_set_track(selected_track)

    # Jab tak video chal raha hai, user ko wait karein
    input("Press Enter to stop playback...")
    player.stop()

# Video ka link specify karein
video_link = "your_video_link_here"

# Function ko call karein
play_video_from_link(video_link)
