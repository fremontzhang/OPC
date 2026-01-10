const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

// Mock Database
let connectedAccounts = [
    {
        id: 'twitter-1',
        platform: 'Twitter', // X
        handle: '@tech_guru_99',
        name: 'Alex Rivera',
        avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Alex',
        status: 'active', // active, syncing, error
        connectedAt: new Date().toISOString()
    },
    {
        id: 'linkedin-1',
        platform: 'LinkedIn',
        handle: 'sarah-jenkins',
        name: 'Sarah Jenkins',
        avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Sarah',
        status: 'active',
        connectedAt: new Date().toISOString()
    }
];

// Available Integrations Data
const availableIntegrations = [
    { id: 'twitter', name: 'X (Twitter)', icon: 'twitter', color: 'bg-black text-white' },
    { id: 'facebook', name: 'Facebook', icon: 'facebook', color: 'bg-blue-600 text-white' },
    { id: 'instagram', name: 'Instagram', icon: 'instagram', color: 'bg-gradient-to-tr from-yellow-400 to-purple-600 text-white' },
    { id: 'linkedin', name: 'LinkedIn', icon: 'linkedin', color: 'bg-blue-700 text-white' },
    { id: 'youtube', name: 'YouTube', icon: 'youtube', color: 'bg-red-600 text-white' },
    { id: 'tiktok', name: 'TikTok', icon: 'video', color: 'bg-black text-white' } // 'video' as placeholder for tiktok
];

// Routes

// GET: Fetch all connected accounts
app.get('/api/accounts', (req, res) => {
    res.json(connectedAccounts);
});

// GET: Fetch available integrations
app.get('/api/integrations', (req, res) => {
    res.json(availableIntegrations);
});

// POST: Connect a new account (Mock)
app.post('/api/connect', (req, res) => {
    const { platformId } = req.body;
    const integration = availableIntegrations.find(i => i.id === platformId);

    if (!integration) {
        return res.status(400).json({ error: 'Integration not found' });
    }

    // Simulate network delay
    setTimeout(() => {
        const newAccount = {
            id: `${platformId}-${Date.now()}`,
            platform: integration.name,
            handle: `@user_${Math.floor(Math.random() * 1000)}`,
            name: 'New User',
            avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=${Date.now()}`,
            status: 'active',
            connectedAt: new Date().toISOString()
        };

        connectedAccounts.push(newAccount);
        res.json(newAccount);
    }, 1500);
});

// DELETE: Disconnect an account
app.delete('/api/accounts/:id', (req, res) => {
    const { id } = req.params;
    connectedAccounts = connectedAccounts.filter(acc => acc.id !== id);
    res.json({ success: true });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
