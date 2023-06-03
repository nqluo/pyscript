import os
import argparse

def compress_video(fAddr, fps=10, resolution=540, rmaudio=True):
	# check fAddr
	if fAddr.lower().endswith('.mov') or fAddr.lower().endswith('.mp4'):
		outputAddr = fAddr[:-4]+'_{}p_{}fps.mp4'.format(resolution, fps)
	else:
		print('Only support .mov or .mp4 files')

	#compress to 540p and 10fps
	os.system("ffmpeg -i {} -vf 'scale=-1:{}, fps={}' {}.mp4".format(fAddr, resolution, fps, outputAddr))

	#remove audio
	if rmaudio ==True:
		outputAddr2 = outputAddr.replace('.mp4','_muted.mp4')
		os.system("ffmpeg -i {}.mp4 -c:v copy -an {}".format(outputAddr, outputAddr2))
		# remove the outputAddr1 file
		os.system("rm {}.mp4".format(outputAddr))
		print('\n-- DONE: \n{} \n-- compress --> \n{}\n'.format(fAddr, outputAddr2))
	else:
		print('\n-- DONE: \n{} \n-- compress --> \n{}\n'.format(fAddr, outputAddr))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Compress video(s) to different resolution, fps')
	parser.add_argument('-i', type = str, dest = 'input', required = True,
						help = 'A .MOV file, or a folder where all .MOV files located')
	parser.add_argument('-r', type = int, dest = 'resolution', default=540, help = 'Resolution, integer, default: 540')
	parser.add_argument('-f', type = int, dest = 'fps', default=10, help = 'frame per second, integer, default: 10')
	parser.add_argument('-m', type = str, dest = 'mute', default='y', help = 'muted the video, Y or N')

	args = parser.parse_args()
	v_input = args.input
	resolution = args.resolution
	fps = args.fps
	mute = args.mute
	if mute == 'y':
		rmaudio = True
	else:
		rmaudio = False

	if os.path.isfile(v_input):
		compress_video(v_input, fps, resolution, rmaudio)
	elif os.path.isdir(v_input):
		video_list = os.listdir(v_input)
		video_list = sorted([item for item in video_list if item.endswith('.MOV')])
		for vName in video_list:
			vAddr = os.path.join(v_input, vName)
			compress_video(vAddr, fps, resolution, rmaudio)
