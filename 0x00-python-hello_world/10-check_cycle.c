#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/* Definition of the linked list node */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
}
listint_t;

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: A pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	return (0);
	slow = list;
	fast = list->next;
	while (fast != NULL && fast->next != NULL)
	{
	if (slow == fast)
	{
	/* Cycle found */
	return (1);
	}
	slow = slow->next;
	fast = fast->next->next;
	}
	/* No cycle found */
	return (0);
}

