import Foundation
import CoreData

struct Match: Identifiable, Codable {
    let id: UUID
    let zayakaScore: Int
    let brianScore: Int
    let winner: String
    let matchDate: Date
    let gameScores: String
    
    init(zayakaScore: Int, brianScore: Int, winner: String, gameScores: String) {
        self.id = UUID()
        self.zayakaScore = zayakaScore
        self.brianScore = brianScore
        self.winner = winner
        self.matchDate = Date()
        self.gameScores = gameScores
    }
}

class MatchStore: ObservableObject {
    @Published var matches: [Match] = []
    @Published var currentZayakaTotal: Int = 0
    @Published var currentBrianTotal: Int = 0
    @Published var gameScores: [String] = []
    
    private let userDefaults = UserDefaults.standard
    private let matchesKey = "savedMatches"
    
    init() {
        loadMatches()
    }
    
    func addGameScore(zayakaScore: Int, brianScore: Int) {
        currentZayakaTotal += zayakaScore
        currentBrianTotal += brianScore
        
        let gameScore = "Zayaka: \(zayakaScore), Brian: \(brianScore)"
        gameScores.append(gameScore)
        
        // Check for winner
        if currentZayakaTotal >= 100 || currentBrianTotal >= 100 {
            endMatch()
        }
    }
    
    func endMatch() {
        let winner = currentZayakaTotal >= 100 ? "Zayaka" : "Brian"
        let gameScoresString = gameScores.joined(separator: "; ")
        
        let match = Match(
            zayakaScore: currentZayakaTotal,
            brianScore: currentBrianTotal,
            winner: winner,
            gameScores: gameScoresString
        )
        
        matches.append(match)
        saveMatches()
        resetCurrentMatch()
    }
    
    func resetCurrentMatch() {
        currentZayakaTotal = 0
        currentBrianTotal = 0
        gameScores = []
    }
    
    func clearAllMatches() {
        matches = []
        saveMatches()
    }
    
    private func saveMatches() {
        if let encoded = try? JSONEncoder().encode(matches) {
            userDefaults.set(encoded, forKey: matchesKey)
        }
    }
    
    private func loadMatches() {
        if let data = userDefaults.data(forKey: matchesKey),
           let decoded = try? JSONDecoder().decode([Match].self, from: data) {
            matches = decoded
        }
    }
    
    func getStatistics() -> (totalMatches: Int, zayakaWins: Int, brianWins: Int, avgZayaka: Double, avgBrian: Double) {
        let totalMatches = matches.count
        let zayakaWins = matches.filter { $0.winner == "Zayaka" }.count
        let brianWins = matches.filter { $0.winner == "Brian" }.count
        
        let avgZayaka = totalMatches > 0 ? Double(matches.map { $0.zayakaScore }.reduce(0, +)) / Double(totalMatches) : 0
        let avgBrian = totalMatches > 0 ? Double(matches.map { $0.brianScore }.reduce(0, +)) / Double(totalMatches) : 0
        
        return (totalMatches, zayakaWins, brianWins, avgZayaka, avgBrian)
    }
}
