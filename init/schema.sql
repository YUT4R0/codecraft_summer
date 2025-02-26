-- create events table
CREATE TABLE Events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  eventName TEXT NOT NULL
);

-- create subcribers table
CREATE TABLE Subscribers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  userName TEXT NOT NULL,
  email TEXT NOT NULL,
  link TEXT,
  event_id INTEGER NOT NULL,
  FOREIGN KEY (event_id) REFERENCES Events (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- create events lunk table
CREATE TABLE Events_link (
  id INTEGER PRIMARY KEY AUTOINCREMENT
  link TEXT,
  event_id INTEGER NOT NULL,
  subscriber_id INTEGER NOT NULL,
  FOREIGN KEY (event_id) REFERENCES Events (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (subscriber_id) REFERENCES Subcribers (id) ON DELETE CASCADE ON UPDATE CASCADE
);