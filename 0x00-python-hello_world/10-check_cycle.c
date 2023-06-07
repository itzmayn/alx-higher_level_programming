#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list; // Initialize two pointers: slow and fast

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next; // Move slow pointer one step ahead
		fast = fast->next->next; // Move fast pointer two steps ahead
		if (slow == fast) // If slow and fast pointers meet, there is a cycle
			return (1);
	}

	return (0); // If no cycle is found, return 0
}
