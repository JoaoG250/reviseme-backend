import { useEffect, useState } from "react";
import { FlatList, StyleSheet } from "react-native";
import { Card, Checkbox, ProgressBar } from "react-native-paper";

import { View, Text } from "../components/Themed";
import { RevisionHistory } from "../interfaces/RevisionHistory";

export default function HistoryTabScreen() {
  const [revisionHistory, setRevisionHistory] = useState<RevisionHistory[]>([]);
  const [revisionProgress, setRevisionProgress] = useState<number>(0);

  // Create test data for revision history on component mount
  useEffect(() => {
    setRevisionHistory([
      {
        id: 1,
        subject: {
          id: 1,
          name: "Mathematics",
          description: "Mathematics subject",
        },
        date: "2020-01-01",
      },
      {
        id: 2,
        subject: {
          id: 2,
          name: "English",
          description: "English subject",
        },
        date: "2020-01-02",
      },
      {
        id: 3,
        subject: {
          id: 3,
          name: "Science",
          description: "Science subject",
        },
        date: "2020-01-03",
      },
    ]);
    setRevisionProgress(95);
  }, []);

  function renderRevisionHistory({ item }: { item: RevisionHistory }) {
    return (
      <Card
        style={{
          marginBottom: 10,
        }}
      >
        <Card.Title
          title={item.subject.name}
          subtitle={item.date}
          right={(props) => <Checkbox {...props} status="checked" disabled />}
        />
      </Card>
    );
  }

  return (
    <View style={styles.container}>
      <View style={styles.historyContainer}>
        <FlatList
          data={revisionHistory}
          renderItem={renderRevisionHistory}
          keyExtractor={(item) => item.id.toString()}
        />
      </View>

      <View
        style={styles.separator}
        lightColor="#eee"
        darkColor="rgba(255,255,255,0.1)"
      />

      <Text style={styles.revisionProgressPercentage}>{revisionProgress}%</Text>
      <View style={styles.progressContainer}>
        <ProgressBar progress={revisionProgress / 100} />
      </View>
      <Text>{revisionProgress}% of revisions completed</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
  },
  historyContainer: {
    width: "100%",
    padding: 16,
  },
  progressContainer: {
    width: "100%",
    padding: 16,
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
  },
  revisionProgressPercentage: {
    fontSize: 40,
    fontWeight: "bold",
  },
});
