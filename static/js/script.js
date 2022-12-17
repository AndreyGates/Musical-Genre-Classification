// To make the submit button appear after uploading
function showButton()
{
    document.getElementById("button").style.display ="block";
}
// To display an uploaded file's name
function showAudioName()
{
    s = document.getElementById("audio-input").value; // this is a full path to the file
    if (s === null || s === "") // if a file wasn't uploaded, no changes
    {
        label.innerHTML = "Нажми меня, чтобы загрузить трек";
        return;
    }

    audio_name = (typeof s==='string' && (s=s.match(/[^\\\/]+$/)) && s[0]) || ''; // and this is its main name

    label = document.getElementById('label');
    label.innerHTML = audio_name;
}
// To delete a previous answer after uploading
function deleteGenreText()
{
    genre_text = document.getElementById("result");
    genre_text.innerHTML = "";
}

audio_input = document.getElementById('audio-input');
audio_input.addEventListener('change', showButton)
audio_input.addEventListener('change', showAudioName)
audio_input.addEventListener('change', deleteGenreText)