using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System.Threading;
using System.Threading.Tasks;
using TestApi.Models;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddDbContext<PosDbContext>(opt => opt.UseSqlite("Data Source=InMemoryTest;Mode=Memory;Cache=Shared"), ServiceLifetime.Singleton);
builder.Services.AddSingleton<IHostedService, DbConnectionOpenService>();

// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

await app.RunAsync();

public class DbConnectionOpenService : IHostedService
{
    private readonly PosDbContext _context;

    public DbConnectionOpenService(PosDbContext context)
    {
        _context = context;
    }

    public async Task StartAsync(CancellationToken cancellationToken)
    {
        await _context.Database.OpenConnectionAsync();
        _context.Database.EnsureCreated();
    }

    public async Task StopAsync(CancellationToken cancellationToken)
    {
        await _context.Database.CloseConnectionAsync();
    }
}