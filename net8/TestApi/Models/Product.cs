namespace TestApi.Models
{
    public class Product
    {
        public string ProductId { get; set; }
        public string? Name { get; set; } = null!;
        public string? Category { get; set; } = null!;
    }
}