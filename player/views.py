from django.shortcuts import render, redirect
from .forms import SongForm

def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list')  # Redirect to a view that displays the list of songs
    else:
        form = SongForm()
        return render(request, 'upload_song.html', {'form': form})



from . models import Song
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})