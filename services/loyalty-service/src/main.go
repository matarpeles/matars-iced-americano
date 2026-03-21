// Loyalty Service - Matar's Iced Americano
// Because regulars deserve the best

package main

import (
	"net/http"
	"github.com/labstack/echo/v4"
)

type Member struct {
	ID        string `json:"id"`
	Name      string `json:"name"`
	Email     string `json:"email"`
	Points    int    `json:"points"`
	Tier      string `json:"tier"`
	JoinedAt  string `json:"joined_at"`
}

func getTier(points int) string {
	switch {
	case points >= 1000:
		return "Platinum"
	case points >= 500:
		return "Gold"
	case points >= 200:
		return "Silver"
	default:
		return "Bronze"
	}
}

func main() {
	e := echo.New()

	e.GET("/health", func(c echo.Context) error {
		return c.JSON(http.StatusOK, map[string]string{
			"status":  "healthy",
			"service": "loyalty-service",
			"version": "3.0.2",
		})
	})

	e.GET("/members/:id", func(c echo.Context) error {
		return c.JSON(http.StatusOK, Member{
			ID:       c.Param("id"),
			Name:     "Coffee Lover",
			Email:    "lover@coffee.com",
			Points:   342,
			Tier:     "Silver",
			JoinedAt: "2024-01-15",
		})
	})

	e.POST("/members/:id/points", func(c echo.Context) error {
		return c.JSON(http.StatusOK, map[string]interface{}{
			"message":    "Points added",
			"new_points": 350,
			"tier":       "Silver",
		})
	})

	e.Logger.Fatal(e.Start(":8080"))
}
