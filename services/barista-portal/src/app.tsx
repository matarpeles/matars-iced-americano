/**
 * Barista Portal - Matar's Iced Americano
 * The barista's command center
 */

import React from 'react';

interface Order {
  id: string;
  customerName: string;
  items: string[];
  status: 'pending' | 'preparing' | 'ready';
  createdAt: string;
}

const mockOrders: Order[] = [
  { id: 'ORD-001', customerName: 'Alex', items: ["Matar's Iced Americano"], status: 'pending', createdAt: '9:15 AM' },
  { id: 'ORD-002', customerName: 'Jordan', items: ['Cold Brew', 'Croissant'], status: 'preparing', createdAt: '9:12 AM' },
  { id: 'ORD-003', customerName: 'Sam', items: ['Iced Latte'], status: 'ready', createdAt: '9:08 AM' },
];

export default function BaristaPortal() {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">☕ Barista Portal</h1>
        <p className="text-gray-600">Matar's Iced Americano - Order Management</p>
      </header>

      <div className="grid grid-cols-3 gap-6">
        {['pending', 'preparing', 'ready'].map((status) => (
          <div key={status} className="bg-white rounded-lg shadow p-4">
            <h2 className="text-lg font-semibold capitalize mb-4">{status}</h2>
            {mockOrders
              .filter((o) => o.status === status)
              .map((order) => (
                <div key={order.id} className="border rounded p-3 mb-2">
                  <div className="font-medium">{order.customerName}</div>
                  <div className="text-sm text-gray-600">{order.items.join(', ')}</div>
                  <div className="text-xs text-gray-400">{order.createdAt}</div>
                </div>
              ))}
          </div>
        ))}
      </div>
    </div>
  );
}
