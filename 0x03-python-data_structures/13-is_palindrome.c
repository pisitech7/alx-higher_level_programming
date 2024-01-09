#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int list_array[2048]; /* Maximum size of list */

	current = *head;

	if (head == NULL || *head == NULL)
		return (1);

	/* Traverse the list and store values in an array */
	int i = 0;
	while (current != NULL)
	{
		list_array[i] = current->n;
		current = current->next;
		i++;
	}

	i--; /* Decrement to point to last element in the array */
	int start = 0;

	/* Check for palindrome by comparing elements from both ends */
	while (start < i)
	{
		if (list_array[start] != list_array[i])
			return (0);
		start++;
		i--;
	}

	return (1);
}

