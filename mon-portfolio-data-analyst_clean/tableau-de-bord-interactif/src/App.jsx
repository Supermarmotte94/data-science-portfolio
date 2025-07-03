import { useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell, LineChart, Line } from 'recharts'
import { BarChart3, TrendingUp, Users, TestTube, MessageSquare, Database, Github, Linkedin, Mail } from 'lucide-react'
import './App.css'

// Données simulées pour les graphiques
const studentPerformanceData = [
  { subject: 'Math', average: 66.1 },
  { subject: 'Reading', average: 69.2 },
  { subject: 'Writing', average: 68.1 }
]

const customerSegmentData = [
  { name: 'Clients Cibles', value: 35, color: '#8884d8' },
  { name: 'Clients Conservateurs', value: 25, color: '#82ca9d' },
  { name: 'Clients Économes', value: 20, color: '#ffc658' },
  { name: 'Clients Dépensiers', value: 20, color: '#ff7300' }
]

const sentimentData = [
  { sentiment: 'Positif', count: 2500 },
  { sentiment: 'Négatif', count: 2500 }
]

const abTestData = [
  { group: 'Contrôle', conversion: 12.04 },
  { group: 'Traitement', conversion: 11.88 }
]

function App() {
  const [activeProject, setActiveProject] = useState('eda')

  const projects = [
    {
      id: 'eda',
      title: 'Analyse Exploratoire de Données',
      description: 'Analyse des performances des étudiants aux examens',
      icon: <BarChart3 className="h-6 w-6" />,
      skills: ['Python', 'Pandas', 'Matplotlib', 'Seaborn', 'Analyse descriptive'],
      insights: [
        'Les filles obtiennent de meilleurs résultats en lecture et écriture',
        'Le niveau d\'éducation parental influence significativement les performances',
        'Les cours de préparation améliorent les scores de 5-10 points en moyenne'
      ]
    },
    {
      id: 'segmentation',
      title: 'Segmentation Client',
      description: 'Analyse de segmentation client avec K-Means clustering',
      icon: <Users className="h-6 w-6" />,
      skills: ['Python', 'Scikit-learn', 'K-Means', 'Clustering', 'Visualisation'],
      insights: [
        '4 segments clients distincts identifiés',
        'Clients cibles : revenus élevés, scores de dépense élevés (35%)',
        'Opportunité d\'augmenter les revenus en ciblant les clients conservateurs'
      ]
    },
    {
      id: 'sentiment',
      title: 'Analyse de Sentiments',
      description: 'Classification de sentiments sur des critiques de films IMDB',
      icon: <MessageSquare className="h-6 w-6" />,
      skills: ['Python', 'NLTK', 'NLP', 'Classification', 'Preprocessing'],
      insights: [
        'Modèle de classification avec 85% de précision',
        'Prétraitement du texte crucial pour la performance',
        'Équilibre parfait entre sentiments positifs et négatifs dans l\'échantillon'
      ]
    },
    {
      id: 'abtest',
      title: 'Test A/B Statistique',
      description: 'Analyse statistique d\'un test A/B sur une page d\'atterrissage',
      icon: <TestTube className="h-6 w-6" />,
      skills: ['Python', 'Statistiques', 'Tests d\'hypothèses', 'Statsmodels'],
      insights: [
        'Pas de différence significative entre les groupes (p-value = 0.19)',
        'Taux de conversion : Contrôle 12.04%, Traitement 11.88%',
        'Recommandation : ne pas déployer la nouvelle page sans modifications'
      ]
    }
  ]

  const currentProject = projects.find(p => p.id === activeProject)

  const renderChart = () => {
    switch (activeProject) {
      case 'eda':
        return (
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={studentPerformanceData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="subject" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="average" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        )
      case 'segmentation':
        return (
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={customerSegmentData}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                {customerSegmentData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        )
      case 'sentiment':
        return (
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={sentimentData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="sentiment" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="count" fill="#82ca9d" />
            </BarChart>
          </ResponsiveContainer>
        )
      case 'abtest':
        return (
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={abTestData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="group" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="conversion" fill="#ffc658" />
            </BarChart>
          </ResponsiveContainer>
        )
      default:
        return null
    }
  }

  return (
    <div className="min-h-screen bg-background p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-foreground mb-2">
            Portfolio d'Analyste de Données
          </h1>
          <p className="text-xl text-muted-foreground mb-4">
            Démonstration de compétences en analyse de données et visualisation
          </p>
          <div className="flex gap-4">
            <Button variant="outline" size="sm" asChild>
              <a href="https://github.com/Supermarmotte94" target="_blank" rel="noopener noreferrer">
                <Github className="h-4 w-4 mr-2" />
                GitHub
              </a>
            </Button>
            <Button variant="outline" size="sm" asChild>
              <a href="https://www.linkedin.com/in/farhan-ali-pieraly/" target="_blank" rel="noopener noreferrer">
                <Linkedin className="h-4 w-4 mr-2" />
                LinkedIn
              </a>
            </Button>
            <Button variant="outline" size="sm" asChild>
              <a href="mailto:pieralyali123@gmail.com">
                <Mail className="h-4 w-4 mr-2" />
                Contact
              </a>
            </Button>
          </div>
        </div>

        {/* Navigation */}
        <Tabs value={activeProject} onValueChange={setActiveProject} className="mb-8">
          <TabsList className="grid w-full grid-cols-4">
            {projects.map((project) => (
              <TabsTrigger key={project.id} value={project.id} className="flex items-center gap-2">
                {project.icon}
                <span className="hidden sm:inline">{project.title.split(' ')[0]}</span>
              </TabsTrigger>
            ))}
          </TabsList>

          {projects.map((project) => (
            <TabsContent key={project.id} value={project.id}>
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Project Info */}
                <Card className="lg:col-span-1">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2">
                      {project.icon}
                      {project.title}
                    </CardTitle>
                    <CardDescription>{project.description}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      <div>
                        <h4 className="font-semibold mb-2">Compétences utilisées :</h4>
                        <div className="flex flex-wrap gap-2">
                          {project.skills.map((skill, index) => (
                            <Badge key={index} variant="secondary">{skill}</Badge>
                          ))}
                        </div>
                      </div>
                      <div>
                        <h4 className="font-semibold mb-2">Insights clés :</h4>
                        <ul className="space-y-1 text-sm text-muted-foreground">
                          {project.insights.map((insight, index) => (
                            <li key={index} className="flex items-start gap-2">
                              <TrendingUp className="h-4 w-4 mt-0.5 text-primary flex-shrink-0" />
                              {insight}
                            </li>
                          ))}
                        </ul>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                {/* Visualization */}
                <Card className="lg:col-span-2">
                  <CardHeader>
                    <CardTitle>Visualisation des données</CardTitle>
                    <CardDescription>
                      Graphique interactif des résultats de l'analyse
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    {renderChart()}
                  </CardContent>
                </Card>
              </div>
            </TabsContent>
          ))}
        </Tabs>

        {/* Summary Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          <Card>
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-muted-foreground">Projets complétés</p>
                  <p className="text-2xl font-bold">4</p>
                </div>
                <Database className="h-8 w-8 text-muted-foreground" />
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-muted-foreground">Datasets analysés</p>
                  <p className="text-2xl font-bold">4</p>
                </div>
                <BarChart3 className="h-8 w-8 text-muted-foreground" />
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-muted-foreground">Techniques utilisées</p>
                  <p className="text-2xl font-bold">12+</p>
                </div>
                <TrendingUp className="h-8 w-8 text-muted-foreground" />
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-muted-foreground">Langages</p>
                  <p className="text-2xl font-bold">Python</p>
                </div>
                <MessageSquare className="h-8 w-8 text-muted-foreground" />
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Footer */}
        <Card>
          <CardContent className="p-6">
            <div className="text-center">
              <h3 className="text-lg font-semibold mb-2">À propos de ce portfolio</h3>
              <p className="text-muted-foreground mb-4">
                Ce portfolio démontre mes compétences en analyse de données à travers quatre projets complets, 
                couvrant l'analyse exploratoire, la segmentation client, l'analyse de sentiments et les tests A/B.
              </p>
              <p className="text-sm text-muted-foreground">
                Créé avec React, Tailwind CSS, et Recharts • Données provenant de Kaggle et GitHub
              </p>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

export default App


