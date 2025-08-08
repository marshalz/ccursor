import Foundation
import CoreData

class DatabaseManager: ObservableObject {
    static let shared = DatabaseManager()
    
    private init() {}
    
    // This is a simple wrapper for UserDefaults since we're using that for storage
    // In a real app, you might use Core Data or other persistence methods
    
    func saveMatches(_ matches: [Match]) {
        if let encoded = try? JSONEncoder().encode(matches) {
            UserDefaults.standard.set(encoded, forKey: "savedMatches")
        }
    }
    
    func loadMatches() -> [Match] {
        if let data = UserDefaults.standard.data(forKey: "savedMatches"),
           let decoded = try? JSONDecoder().decode([Match].self, from: data) {
            return decoded
        }
        return []
    }
    
    func clearAllMatches() {
        UserDefaults.standard.removeObject(forKey: "savedMatches")
    }
}
