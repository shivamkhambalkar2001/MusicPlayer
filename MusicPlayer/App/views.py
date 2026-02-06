from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, Http404
from .models import Song
from .forms import SongForm
import os
from django.contrib import messages

def main_view(request):
    return render(request, 'main.html')

#Add songs Functionality 
def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('App:index')
    else:
        form = SongForm()
    context = {'form': form}
    return render(request, 'add_song.html', context)

#Show All Songs 
def index(request):
    songs = Song.objects.all()
    print(songs,'line no 68')
    return render(request, 'index.html', {'songs': songs})

# delete song functionality 
def delete_confirmation(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'delete_confirmation.html', {'song': song})

def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'POST':
        try:
            if song.audio_file and os.path.isfile(song.audio_file.path):
                os.remove(song.audio_file.path)
            if song.image_file and os.path.isfile(song.image_file.path):
                os.remove(song.image_file.path)
            
            song.delete()
            messages.success(request, f'Song "{song.title}" by {song.artist} has been deleted successfully.')

        except PermissionError as e:
            messages.error(request, "Could not delete the file. It is being used by another process.")
            return redirect('App:delete_confirmation', song_id=song.id)

        except Exception as e:
            messages.error(request, "An unexpected error occurred while trying to delete the song.")
            return redirect('App:delete_confirmation', song_id=song.id)

        return redirect('App:index')

    return redirect('App:delete_confirmation', song_id=song.id)

#download functionality
def download_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if song.audio_file:
        response = FileResponse(song.audio_file.open('rb'), as_attachment=True, filename=song.audio_file.name)
        return response
    else:
        raise Http404("Song file not found")
    

#searching functionality 
def search_songs(request):
    query = request.GET.get('q')
    song = None
    if query:
        song = Song.objects.filter(title__icontains=query).first()  # Get the first matching song
    context = {'song': song}
    return render(request, 'search_song.html', context)

    
