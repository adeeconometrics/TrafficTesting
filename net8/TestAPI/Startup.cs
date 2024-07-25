void ConfigureServices(IServiceCollection services)
{
    services.AddDbContext<MyDbContext>();
    services.AddControllers();
}