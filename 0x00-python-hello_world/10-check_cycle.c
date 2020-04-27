#include "lists.h"

/**
 * check_cycle - check for cycle in linked list
 * @list: provided list
 * Return: 1 if list contains a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list)
	{
		slow = list;
		fast = list;
		while (fast->next->next)
		{
			slow = slow->next;
			fast = fast->next->next;
			if (slow == fast)
				return (1);
		}
	}

	return (0);
}
