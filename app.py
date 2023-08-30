import streamlit as st
from pytube import YouTube
from streamlit_extras.stateful_button import button

def tittle():
    yt = YouTube(url)
    st.write(yt.title)
    thumbnail = yt.thumbnail_url
    st.image(thumbnail,width=400)
    st.write(f"Total Views {yt.views}")
    st.write(f"Channel Name {yt.author}")

def high_resolution():
    yt = YouTube(url)
    with st.spinner("wait"):
        st.write("downloading")
    stream = yt.streams.filter(resolution='720p').first()
    st.write(f"Size {stream.filesize_mb} MB")
    big_url = stream.url
    st.markdown(f'<a href="{big_url}" target="_blank">Download</a>', unsafe_allow_html=True)

def medium_resolution():
    yt = YouTube(url)
    with st.spinner("wait"):
        st.write("downloading...")
    stream = yt.streams.filter(resolution="360p").first()
    st.write(f"Size {stream.filesize_mb} Mb")
    big_url = stream.url
    st.markdown(f'<a href="{big_url}" target="_blank">Download</a>', unsafe_allow_html=True)
    
        
        

def low_resolution():
    yt = YouTube(url)
    with st.spinner("wait"):
        st.write("Downloading....")
    steam = yt.streams.filter(resolution="144p").first()
    st.write(f"Size {steam.filesize_mb} MB")
    big_url = steam.url
    st.markdown(f'<a href="{big_url}" target="_blank">Download</a>', unsafe_allow_html=True)


st.title("Youtube video downloader")
try:
    url = st.text_input("Enter Video link")
    if button("download", key="download"):
        tittle()
        with st.expander("Select resolution"):
            if button("High resolution(720p)",key="720p"):
                high_resolution()
            if button("Medium reslution(360p)",key='360p'):
                medium_resolution()
            if button("Low resulation (144p)",key="144p"):
                low_resolution()
except Exception as e:
    st.warning("Enter valid Link")
    if button("see error",key="error button"):
        st.warning(e)







