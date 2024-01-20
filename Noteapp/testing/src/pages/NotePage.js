import React, { useEffect, useState } from "react";

import { Link, useParams } from "react-router-dom";
import { ReactComponent as ArrowLeft } from "../assets/arrow-left.svg";

const NotePage = () => {
  const { id } = useParams();
  const [note, setNote] = useState(null);
  useEffect(() => {
    getNote();
  }, []);

  const updateNote = async () => {
    await fetch(`/api/notes/${id}`, {
      method: "PUT",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(note),
    });
    console.log(
      "---------------------------------------------------------------"
    );
  };

  const createNote = async () => {
    await fetch(`/api/notes/`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(note),
    });
  };

  const deletenote = async () => {
    await fetch(`/api/notes/${id}`, {
      method: "DELETE",
      headers: {
        "content-type": "application/json",
      },
    });
  };

  let handlesummit = () => {
    updateNote();
    if (id !== "new" && !note.body) {
      deletenote();
    } else if (id !== "new") {
      updateNote();
    } else if (id === "new" && note != null) {
      createNote();
    }
  };

  const getNote = async () => {
    if (id === "new") return;
    let response = await fetch(`/api/notes/${id}`);
    let data = await response.json();
    console.log(data);
    setNote(data);
  };

  return (
    <div className="note">
      <div className="note-header">
        <h3>
          <Link to={"/"}>
            <ArrowLeft onClick={handlesummit} />
          </Link>
        </h3>
        <Link to={"/"}>
          {id !== "new" ? (
            <button onClick={deletenote}>Delete</button>
          ) : (
            <button onClick={handlesummit}>Done</button>
          )}
        </Link>
      </div>
      <textarea
        onChange={(e) => {
          setNote({ ...note, body: e.target.value });
        }}
        value={note?.body}
      ></textarea>
    </div>
  );
};

export default NotePage;
