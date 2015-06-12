import cv2
import os
import argparse
import sys

def write_video_frames(video_path, output_path = None, convert_to_grayscale = False):
    try:
        video = cv2.VideoCapture(video_path)
        frame_count = 0
        success = True
        while success:
            success,frame = video.read()
            if convert_to_grayscale:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            full_output_path = os.path.join(output_path, "frame_%d.jpg" % frame_count)
            cv2.imwrite(full_output_path, frame)
            frame_count += 1
            print "Writing frame %d to %s \r" % (frame_count, output_path),
            sys.stdout.flush()
        print "Wrote %d frames to %s" % (frame_count, output_path)
        return output_path
    except:
        raise Exception("Error reading from file %s" % video_path)

def run(video_path, output_path):
    if output_path is None:
        output_path = "%s%s" % (video_path, ".frames/")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    write_video_frames(video_path, output_path)
        
def run_with_args(args):
    input_video = args['video']
    output_path = args['output']
    run(input_video, output_path)

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--video", help="input video", required=True)
parser.add_argument("-o", "--output", help="output directory", required=False)
args = vars(parser.parse_args())
run_with_args(args)

