/**
 * Menu Service - Matar's Iced Americano
 * The source of truth for what we serve
 */

const express = require('express');
const app = express();

app.use(express.json());

const menu = {
  drinks: [
    { id: 'iced-americano', name: "Matar's Iced Americano", price: 4.50, category: 'signature' },
    { id: 'cold-brew', name: 'Cold Brew', price: 4.00, category: 'coffee' },
    { id: 'iced-latte', name: 'Iced Latte', price: 5.00, category: 'coffee' },
    { id: 'matcha-latte', name: 'Iced Matcha Latte', price: 5.50, category: 'specialty' },
  ],
  customizations: [
    { id: 'extra-shot', name: 'Extra Shot', price: 0.75 },
    { id: 'oat-milk', name: 'Oat Milk', price: 0.50 },
    { id: 'vanilla', name: 'Vanilla Syrup', price: 0.50 },
  ]
};

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', service: 'menu-service', version: '4.1.0' });
});

app.get('/menu', (req, res) => {
  res.json(menu);
});

app.get('/menu/drinks', (req, res) => {
  res.json(menu.drinks);
});

app.get('/menu/drinks/:id', (req, res) => {
  const drink = menu.drinks.find(d => d.id === req.params.id);
  if (!drink) return res.status(404).json({ error: 'Drink not found' });
  res.json(drink);
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Menu Service running on port ${PORT}`);
});
