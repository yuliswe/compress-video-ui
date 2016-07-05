.PHONY: build
.PHONY: default
.PHONY: clean
.PHONY: test
.PHONY: copy-bin
.PHONY: copy-pyqt
.PHONY: run
	
default:
	make build
	make test

build:
	make pyqt
	make clean
	pyinstaller python/main.py
	mkdir ./dist/preset/
	mkdir ./dist/app/
	mkdir ./dist/update/
	mv ./dist/main ./dist/app/ui
	touch ./dist/LICENSE
	touch ./dist/update/VERSION
	make copy-bin
	rm -rf ./build
	rm main.spec
	
run:
	cd dist && ./app/ui/main --preset-dir ./config --compress-bin ./app/compress-video.exe --update-bin ./update/compress-video-update.exe --update-cfg ./update/compress-video-update.cfg
	
clean:
	rm -rf ./dist
	rm -rf ./build
	rm -f main.spec
	
test:
	make copy-bin
	echo "test" > ./dist/LICENSE
	cp -rf ./test/preset ./dist/
	cp -rf ./test/compress-video-update.cfg ./dist/update/compress-video-update.cfg
	cd dist && ../python/main.py --preset-dir ./preset --compress-bin ./app/compress-video.exe --update-bin ./update/compress-video-update.exe --update-cfg ./update/compress-video-update.cfg
	
copy-bin:
	cp `which compress-video-exe` ./dist/app/compress-video.exe
	cp `which compress-video-update-exe` ./dist/update/compress-video-update.exe
	
pyqt:
	pyuic5 -o ./python/mainwindow_ui.py -x ./mainwindow.ui
	pyuic5 -o ./python/filelistitem_ui.py -x ./plugin/filelistitem.ui
	pyrcc5 -o ./python/mainwindow_rc.py ./resource/mainwindow.qrc
