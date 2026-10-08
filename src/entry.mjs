import { LibreDwg, Dwg_File_Type, createModule } from '@mlightcad/libredwg-web';

window.DwgEngine = {
  async init(wasmBinary) { const m = await createModule({ wasmBinary }); return LibreDwg.createByWasmInstance(m); },
  Dwg_File_Type
};
