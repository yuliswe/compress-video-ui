default:
	make clean
	pyinstaller python/main.py --name app
	mkdir ./dist/config
	
run:
	make
	./dist/main/main
	
clean:
	rm -rf ./dist
	rm -rf ./build
	