import React, { useEffect, useState } from "react";
import "./App.css";
import { get, create, remove, patch } from "./services/requests";

import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import ApprovalItem from "@mui/icons-material/Approval";
import DeleteIcon from "@mui/icons-material/DeleteOutlined";
import MenuItem from "@mui/material/MenuItem";
import {
  GridRowsProp,
  GridRowModesModel,
  DataGrid,
  GridColDef,
  GridToolbarContainer,
  GridActionsCellItem,
  GridEventListener,
  GridRowId,
  GridRowModel,
  GridRowEditStopReasons,
  GridSlots,
} from "@mui/x-data-grid";

import { FormControl, Stack } from "@mui/material";
import { randomArrayItem } from "@mui/x-data-grid-generator";
import ModalUnstyled from "./components/modal/Modal";

const roles = ["Market", "Finance", "Development"];

interface EditToolbarProps {
  setRows: (newRows: (oldRows: GridRowsProp) => GridRowsProp) => void;
  setRowModesModel: (
    newModel: (oldModel: GridRowModesModel) => GridRowModesModel
  ) => void;
}

function EditToolbar(_: EditToolbarProps) {
  return (
    <GridToolbarContainer>
      <h1 style={{ paddingLeft: "5px" }}>Solicitudes</h1>
    </GridToolbarContainer>
  );
}

interface RequestsRow {
  id: number;
  nombre: string;
  apellido: string;
  identificacion: string;
  edad: number;
  estado_solicitud: string;
  afinidad_magica: string;
}

interface CreateRow {
  nombre: string;
  apellido: string;
  identificacion: string;
  edad: number;
  afinidad_magica: string;
}

function App() {
  const [rows, setRows] = useState<RequestsRow[]>([]);
  const [rowModesModel, setRowModesModel] = React.useState<GridRowModesModel>(
    {}
  );
  const [nombre, setNombre] = useState("");
  const [apellido, setApellido] = useState("");
  const [identificacion, setIdentificacion] = useState("");
  const [edad, setEdad] = useState(0);
  const [afinidadMagica, setAfinidadMagica] = useState("");
  const [open, setOpen] = useState(false);
  const handleClose = () => setOpen(false);

  const fetchData = async () => {
    const response = await get("solicitudes");
    if (response.status === 200) {
      setRows(response.data);
    }
  };

  const deleteRow = async (id: number) => {
    const response = await remove(`solicitud/${id}`);
    if (response.status === 200) {
      await fetchData();
    }
  };

  const handleSubmit = async (event: any) => {
    event.preventDefault();

    const response = await create("solicitudes", {
      nombre: nombre,
      apellido: apellido,
      identificacion: identificacion,
      edad: edad,
      afinidad_magica: afinidadMagica,
    });

    if (response.status === 200) {
      setRows(response.data);
      cleanForm();
    }

    await fetchData();
  };

  const cleanForm = () => {
    setNombre("");
    setApellido("");
    setIdentificacion("");
    setEdad(0);
    setAfinidadMagica("");
  };

  const handlePatch = async (id: number) => {
    const response = await patch(
      `solicitudes/${id}/estatus`,
      JSON.stringify({ estado_solicitud: "aceptada" })
    );

    if (
      response.status === 200 &&
      response.data.message === `Solicitud aceptada con id: ${id}`
    ) {
      setOpen(true);
    }

    fetchData();
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleRowEditStop: GridEventListener<"rowEditStop"> = (
    params,
    event
  ) => {
    if (params.reason === GridRowEditStopReasons.rowFocusOut) {
      event.defaultMuiPrevented = true;
    }
  };

  const handleApprovalRequest = (id: GridRowId) => () => {
    handlePatch(parseInt(id.toString()));
  };

  const handleDeleteClick = (id: GridRowId) => () => {
    deleteRow(parseInt(id.toString()));
  };

  const processRowUpdate = (newRow: GridRowModel) => {
    const updatedRow = { ...newRow, isNew: false };
    return updatedRow;
  };

  const handleRowModesModelChange = (newRowModesModel: GridRowModesModel) => {
    setRowModesModel(newRowModesModel);
  };

  const columns: GridColDef[] = [
    { field: "nombre", headerName: "Nombre", width: 120, editable: true },
    {
      field: "apellido",
      headerName: "Apellido",
      width: 120,
      editable: true,
    },
    {
      field: "identificacion",
      headerName: "Identificacion",
      width: 120,
      editable: true,
    },
    {
      field: "edad",
      headerName: "Edad",
      width: 80,
      editable: true,
      type: "number",
    },
    {
      field: "afinidad_magica",
      headerName: "Afinidad Magica",
      width: 180,
      editable: true,
      type: "singleSelect",
      valueOptions: ["Oscuro", "Fuego", "Agua", "Tierra", "Viento"],
    },
    {
      field: "estado_solicitud",
      headerName: "Estado Solicitud",
      width: 180,
      editable: false,
      type: "string",
    },
    {
      field: "actions",
      type: "actions",
      headerName: "Actions",
      width: 100,
      cellClassName: "actions",
      getActions: ({ id }) => {
        return [
          <GridActionsCellItem
            key={id}
            icon={<ApprovalItem />}
            label="Approve"
            className="textPrimary"
            onClick={handleApprovalRequest(id)}
            color="inherit"
          />,
          <GridActionsCellItem
            key={id}
            icon={<DeleteIcon />}
            label="Delete"
            onClick={handleDeleteClick(id)}
            color="inherit"
          />,
        ];
      },
    },
  ];

  const Afinidades = [
    {
      label: "Oscuro",
      value: "Oscuro",
    },
    {
      label: "Luz",
      value: "Luz",
    },
    {
      label: "Fuego",
      value: "Fuego",
    },
    {
      label: "Agua",
      value: "Agua",
    },
    {
      label: "Tierra",
      value: "Tierra",
    },
    {
      label: "Viento",
      value: "Viento",
    },
  ];

  return (
    <div className="App">
      <ModalUnstyled open={open} onClose={handleClose} />
      <div className="Container-app">
        <Box
          sx={{
            height: "90vh",
            width: "100%",
            "& .actions": {
              color: "text.secondary",
            },
            "& .textPrimary": {
              color: "text.primary",
            },
            boxShadow: 2,
          }}
        >
          <img
            src="https://cdn.antaranews.com/cache/1200x800/2023/11/15/Black-Clover.png"
            width={"100%"}
            alt=""
            style={{ marginBottom: "-15vh" }}
          />
          <form autoComplete="off" onSubmit={handleSubmit}>
            <FormControl>
              <Stack spacing={2} direction="row" sx={{ marginBottom: 4 }}>
                <TextField
                  type="text"
                  variant="outlined"
                  color="secondary"
                  label="Nombre"
                  onChange={(e) => setNombre(e.target.value)}
                  value={nombre}
                  fullWidth
                  required
                />
                <TextField
                  type="text"
                  variant="outlined"
                  color="secondary"
                  label="Apellido"
                  onChange={(e) => setApellido(e.target.value)}
                  value={apellido}
                  fullWidth
                  required
                />
              </Stack>
              <Stack spacing={2} direction="row" sx={{ marginBottom: 4 }}>
                <TextField
                  type="text"
                  variant="outlined"
                  color="secondary"
                  label="Identificacion"
                  onChange={(e) => setIdentificacion(e.target.value)}
                  value={identificacion}
                  fullWidth
                  required
                  sx={{ mb: 4 }}
                />
                <TextField
                  type="number"
                  variant="outlined"
                  color="secondary"
                  label="Edad"
                  onChange={(e) => setEdad(parseInt(e.target.value))}
                  value={edad}
                  required
                  fullWidth
                  sx={{ mb: 4 }}
                />
              </Stack>

              <TextField
                select
                variant="outlined"
                color="secondary"
                defaultValue="Oscuro"
                label="Afinidad Magica"
                onChange={(e) => setAfinidadMagica(e.target.value)}
                value={afinidadMagica}
                fullWidth
                required
                sx={{ mb: 4 }}
              >
                {Afinidades.map((option) => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>
              <Button variant="outlined" color="secondary" type="submit">
                Registrar
              </Button>
            </FormControl>
          </form>
        </Box>
        <Box
          sx={{
            height: "auto",
            width: "100%",
            "& .actions": {
              color: "text.secondary",
            },
            "& .textPrimary": {
              color: "text.primary",
            },
          }}
        >
          <DataGrid
            rows={rows}
            columns={columns}
            editMode="row"
            rowModesModel={rowModesModel}
            onRowModesModelChange={handleRowModesModelChange}
            onRowEditStop={handleRowEditStop}
            processRowUpdate={processRowUpdate}
            slots={{
              toolbar: EditToolbar as GridSlots["toolbar"],
            }}
            slotProps={{
              toolbar: { setRows, setRowModesModel },
            }}
          />
        </Box>
      </div>
    </div>
  );
}

export default App;
