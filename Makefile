default:
	make clean
	pyinstaller python/main.py
	mkdir ./dist/config
	
run:
	make
	./dist/main/main
	
clean:
	rm -r ./dist
	