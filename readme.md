## Image Processing Utils
`img_proc_utils` contains a set of utilities to process and analyze images and video.

### Requirements
The code below uses Python 2.7. Most of the utilities require OpenCV.

### Converting Video to Frames
The `video_framerizer` script can be used to convert a video into a series of frames. Given a local video file, the usage model is:

```python
python video_framerizer.py --video someVideo.mp4
```

This will create a directory called `someVideo.mp4.frames` in the same directory as the video, with images for each frame of the video. If you would like to specifiy a different location for the frames directory, it can be specified via

```python
python video_framerizer.py --video someVideo.mp4 --output path_to_some_different_directory
```


