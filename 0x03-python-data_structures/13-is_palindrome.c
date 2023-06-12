#include "lists.h"

/**
 * pal - recursive helper function to determine if llst is palindrom
 * @start: start position of list
 * @end: end position of list
 */

int pal(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (1);

	if (pal(start, end->next) == 1 && (*start)->n == end->n)
	{
		*start = (*start)->next;
		return (1);
	}

	return (0);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: list to check
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	return (pal(head, *head));
}
