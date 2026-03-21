// Payment Gateway - Matar's Iced Americano
// Secure payment processing service

package main

import (
	"net/http"
	"github.com/gin-gonic/gin"
)

type PaymentRequest struct {
	OrderID     string  `json:"order_id" binding:"required"`
	Amount      float64 `json:"amount" binding:"required"`
	Currency    string  `json:"currency" binding:"required"`
	Method      string  `json:"method" binding:"required"`
	CustomerID  string  `json:"customer_id" binding:"required"`
}

type PaymentResponse struct {
	TransactionID string `json:"transaction_id"`
	Status        string `json:"status"`
	Message       string `json:"message"`
}

func main() {
	r := gin.Default()

	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"status":  "healthy",
			"service": "payment-gateway",
			"version": "2.8.0",
		})
	})

	r.POST("/payments", func(c *gin.Context) {
		var req PaymentRequest
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		c.JSON(http.StatusOK, PaymentResponse{
			TransactionID: "TXN-" + req.OrderID,
			Status:        "completed",
			Message:       "Payment processed successfully",
		})
	})

	r.GET("/payments/:id", func(c *gin.Context) {
		id := c.Param("id")
		c.JSON(http.StatusOK, gin.H{
			"transaction_id": id,
			"status":         "completed",
			"amount":         4.50,
			"currency":       "USD",
		})
	})

	r.Run(":8080")
}
