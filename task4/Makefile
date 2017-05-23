CC=gcc
CFLAGS=-c -Wall
EXECUTABLE=check_hashes

all: $(EXECUTABLE)

$(EXECUTABLE): check_hashes.o
	$(CC) $^ -o $@

check_hashes.o: check_hashes.c
	$(CC) $(CFLAGS) $^

.PHONY: clean

clean:
	rm *.o $(EXECUTABLE)
