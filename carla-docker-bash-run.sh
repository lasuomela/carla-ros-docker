docker run \
 -p 2000-2002:2000-2002 \
 --runtime=nvidia \
 --gpus 'all,"capabilities=graphics,utility,display,video,compute"' \
 -e SDL_VIDEODRIVER='offscreen' \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 -it \
 carlasim/carla:0.9.11 \
 ./CarlaUE4.sh
