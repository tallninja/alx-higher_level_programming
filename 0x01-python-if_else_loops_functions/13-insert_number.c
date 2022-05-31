#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head
 * @number: number
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		return (*head = new_node);
	}
	else
	{
		while (current_node && current_node->n < number)
		{
			temp = current_node;
			current_node = current_node->next;
		}
		temp->next = new_node;
		new_node->next = current_node;
	}

	return (new_node);
}
