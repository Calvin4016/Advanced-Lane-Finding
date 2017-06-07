''' 
Supports mp4 video format as of now. Individual image can be processed using
the pipeline and find line functions provided.
'''
from moviepy.editor import VideoFileClip
from IPython.display import HTML
Import image_processing_functions

# Set up lines for left and right
left_lane = Line()
right_lane = Line()
white_output = 'lane_finding.mp4'
clip1 = VideoFileClip("YOUR_VIDEO_FILE_GOES_HERE.mp4")
white_clip = clip1.fl_image(process_image) #NOTE: this function expects color images!!
%time white_clip.write_videofile(white_output, audio=False)