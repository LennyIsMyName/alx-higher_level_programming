#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - print values
 * @h: head to the first node
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *tp = h;
	int num = 0;

	while (tp != NULL)
	{
		num = num + 1;
		printf("%d\n", tp->n);
		tp = tp->next;
	}
	return (num);
}
