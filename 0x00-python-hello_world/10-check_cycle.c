#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: list
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list, *further = list;

	while (current != NULL && further != NULL && further->next != NULL)
	{
		current = current->next;
		further = further->next->next;

		if (current == further)
			return (1);
	}

	return (0);
}
