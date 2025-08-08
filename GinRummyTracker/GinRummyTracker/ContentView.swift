import SwiftUI

struct ContentView: View {
    @StateObject private var matchStore = MatchStore()
    
    var body: some View {
        TabView {
            ScoreEntryView()
                .environmentObject(matchStore)
                .tabItem {
                    Image(systemName: "plus.circle.fill")
                    Text("Score Entry")
                }
            
            HistoryView()
                .environmentObject(matchStore)
                .tabItem {
                    Image(systemName: "list.bullet")
                    Text("History")
                }
            
            StatsView()
                .environmentObject(matchStore)
                .tabItem {
                    Image(systemName: "chart.bar.fill")
                    Text("Statistics")
                }
        }
        .accentColor(.blue)
    }
}

#Preview {
    ContentView()
}
