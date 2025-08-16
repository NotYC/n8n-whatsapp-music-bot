from flask import Flask, request, send_file, jsonify
import subprocess
import os
import glob

app = Flask(__name__)

DOWNLOAD_DIR = "..\\flask\\"

@app.route('/download', methods=['POST'])
def download_song():
    data = request.get_json()
    song_link = data.get("link")
    if not song_link:
        return jsonify({"error": "No song-link provided"}), 400

    # Ensure the download directory exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Use spotdl to download the song into the downloads folder with 96k bitrate
    download_cmd = [
        "spotdl", song_link,
        "--bitrate", "96k",
        "--output", f"{DOWNLOAD_DIR}/"
    ]
    result = subprocess.run(download_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("stdout:", result.stdout.decode())
    print("stderr:", result.stderr.decode())

    # Find the latest downloaded MP3 file
    mp3_files = sorted(glob.glob(f"{DOWNLOAD_DIR}/*.mp3"), key=os.path.getmtime, reverse=True)
    if not mp3_files:
        return jsonify({"error": "No MP3 file found after download"}), 500

    song_path = mp3_files[0]

    try:
        # Send the MP3 file as response
        return send_file(song_path, mimetype="audio/mpeg", as_attachment=True)
    finally:
        # Clean up: delete the file after sending
        try:
            os.remove(song_path)
        except Exception as e:
            print(f"Error deleting file: {e}")

@app.route('/cleanup', methods=['DELETE'])
def cleanup_songs():
    deleted = []
    failed = []

    # Find all MP3 files in the directory
    mp3_files = glob.glob(os.path.join(DOWNLOAD_DIR, "*.mp3"))

    for file_path in mp3_files:
        try:
            os.remove(file_path)
            deleted.append(os.path.basename(file_path))
        except Exception as e:
            failed.append({"file": os.path.basename(file_path), "error": str(e)})

    return jsonify({
        "deleted": deleted,
        "failed": failed,
        "status": "done"
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=5555, host="0.0.0.0")
