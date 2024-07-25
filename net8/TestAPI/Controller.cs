using Microsoft.AspNetCore.Mvc;

namespace TodoApi.Models;


[HttpPost]
public async Task<ActionResult<TodoItem>> CreateTodoItem(TodoItem todoItem)
{
    _context.TodoItems.Add(todoItem);
    await _context.SaveChangesAsync();

    return CreatedAtAction(
        nameof(GetTodoItem),
        new { id = todoItem.Id },
        todoItem);
}