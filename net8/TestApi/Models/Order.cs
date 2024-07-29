namespace TestApi.Models
{
    public class Order
    {
        public string OrderId { get; set; }
        public string? UserId { get; set; } = null!;
        public string? ProductId { get; set; } = null!;
        public int Quantity { get; set; }
        public double TotalPrice { get; set; }
        public string? OrderDate { get; set; } = null!;
        public string? ShippingAddress { get; set; } = null!;
        public string? PaymentMethod { get; set; } = null!;
    }
}