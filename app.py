import streamlit as st
import pandas as pd
import numpy as np

from spotify_process import get_episode
from spotify_process import get_show
from spotify_process import process_mp3

#from utils import set_environment_variables

my_id = '1453fef31f0a4e70ad8fa2989e6db891'
my_secret = 'f6ef11e892c34f9fbd0c284d52d8d417'
target = '36gVeeoYns1RBASPLhAYeJ'
#url = "https://media.transistor.fm/68ecbcdf/c5fe07ff.mp3"

# Set up the page configuration
st.set_page_config(layout="wide")

# Initialize settings

def main():
    #set_environment_variables()
    st.title("podcast2learn")

    episode_id = st.text_input("Enter Episode ID to here:")
    if episode_id and st.button("Process Start"):
        with st.spinner("Processing..."):
            print(episode_id)
            episode = get_episode(my_id, my_secret, episode_id)
            st.success("Episode exists!")
            st.write("Current episode:", episode['name'])
            st.write("Date:", episode['release_date'])
            st.write("Link: ",episode['audio_preview_url'])
            st.audio(episode['audio_preview_url'], format="audio/mpeg", loop=True)
            print(episode['audio_preview_url'])
            #st.audio(url, format="audio/mpeg", loop=False)

            col1, col2 = st.columns([1,2])

            with col1:
                st.title("Original Episode")
                shows = get_show(my_id, my_secret, target)
                episodes_container = st.container()
                with episodes_container:
                    for episode in shows:
                        st.write(episode['name'])

            with col2:
                st.title("Tuned Episode")
                if episode_id:
                    episode = get_episode(my_id, my_secret, episode_id)
                    text = process_mp3(episode['audio_preview_url'])
                    st.write(text)

if __name__ == "__main__":
    main()