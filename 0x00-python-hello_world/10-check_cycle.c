#include "lists.h"

/**
 * check_cycle - Checks if there s loop in a single linked list
 * @list: Linked list to check
 *
 * Return: 0 if there is no loop, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;
	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
