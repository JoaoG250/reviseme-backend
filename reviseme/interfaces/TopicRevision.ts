import { Topic } from "./Topic";

type TopicRevisionStatus = "PENDING" | "COMPLETED" | "FAILED";

export interface TopicRevision {
  id: number;
  topic: Topic;
  dateRevision1d: string;
  dateRevision7d: string;
  dateRevision30d: string;
  dateRevision90d: string;
  statusRevision1d: TopicRevisionStatus;
  statusRevision7d: TopicRevisionStatus;
  statusRevision30d: TopicRevisionStatus;
  statusRevision90d: TopicRevisionStatus;
}