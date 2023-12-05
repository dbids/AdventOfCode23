#include <stdio.h>
#include <execinfo.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
// Stack Trace
void handler(int sig) {
  void *array[10];
  size_t size;

  // get void*'s for all entries on the stack
  size = backtrace(array, 10);

  // print out all the frames to stderr
  fprintf(stderr, "Error: signal %d:\n", sig);
  backtrace_symbols_fd(array, size, STDERR_FILENO);
  exit(1);
}

// Driver code
int main()
{
  // Install stack trace exception handler
  signal(SIGSEGV, handler);   // install our handler

  // Main code
	FILE* ptr = fopen("day5_sample.txt", "r");
	if (ptr == NULL) {
		printf("no such file.");
		return 0;
	}

	int * first;
  int * second;
  int * third;
  int * fourth;
	fscanf(ptr, "seeds: %d %d %d %d ", first, second, third, fourth);
	printf("%d %d %d %d\n", *first, *second, *third, *fourth);

	return 0;
}
