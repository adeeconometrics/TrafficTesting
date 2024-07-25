using Microsoft.EntityFrameworkCore;

public class MyDbContext : DbContext
{
    public DbSet<Item> Items { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder options)
        => options.UseSqlite("Data Source=TestAPI.db");
}