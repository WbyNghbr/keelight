v4l2-ctl --set-edid=file=/home/anatoly/capture_init/1080P60EDID.txt
v4l2-ctl --set-fmt-video=pixelformat=UYVY
sleep 5
v4l2-ctl --set-dv-bt-timings query
v4l2-ctl -V
