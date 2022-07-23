#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_loop - an infinite loop
 *
 * Return: 0
 */
int infinite_loop(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	infinite_loop();
	return (0);
}
