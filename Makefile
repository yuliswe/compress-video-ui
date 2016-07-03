default:
	make pyqt
	make clean
	pyinstaller python/main.py --name app
	mkdir ./dist/config
	make copy-bin
	./dist/app/app --cfg-dir ./config --bin-dir ./bin
	
	
clean:
	rm -rf ./dist
	rm -rf ./build
	
test:
	make copy-bin
	python3 python/main.py --cfg-dir ./config --bin-dir ./bin
	
copy-bin:
	cp `which compress-video-exe` ./bin/compress-video.exe
	cp `which compress-video-update-exe` ./bin/compress-video-update.exe
	
pyqt:
	pyuic5 -o ./qt/mainwindow_ui.py -x ./mainwindow.ui
	pyuic5 -o ./qt/filelistitem_ui.py -x ./plugin/filelistitem.ui
	pyrcc5 -o ./qt/mainwindow_rc.py ./resource/mainwindow.qrc
